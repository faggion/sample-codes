#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/errno.h>
#include <linux/fs.h>
#include <asm/uaccess.h>
#include <linux/random.h>
#include <linux/slab.h>

#include <linux/poll.h>
#include <linux/sched.h>

MODULE_AUTHOR("PSI");
MODULE_DESCRIPTION("\"poll world\" MODULE");
MODULE_LICENSE("GPL");

#define BUF_SIZ 64
#define MAJOR_ID 280

static unsigned char msg[BUF_SIZ];
static int buf_pos = 0;
static wait_queue_head_t write_q;
static wait_queue_head_t read_q;

static int poll_open( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "poll_dev:open: major=%d, minor=%d\n",
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev));
    return 0;
}

static int poll_release( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "poll_dev:release\n");
    return 0;
}

static ssize_t poll_read(struct file* filp, char* buf, size_t count, loff_t* pos ){
    int copy_len;
    int i;
    while ( buf_pos == 0 ) {
        if ( filp->f_flags & O_NONBLOCK ) {
            return -EAGAIN;
        }
        if ( wait_event_interruptible( read_q, ( buf_pos != 0 ) ) )
            return -ERESTARTSYS;
    }
    if ( count > buf_pos )
        copy_len = buf_pos;
    else
        copy_len = count;

    if ( copy_to_user( buf, msg, copy_len ) ) {
        return -EFAULT;
    }
    *pos += copy_len;

    for ( i = copy_len; i < buf_pos; i ++ )
        msg[ i - copy_len ] = msg[i];

    buf_pos -= copy_len;
    wake_up_interruptible( &write_q );
    return copy_len;
}

static ssize_t poll_write(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    int copy_len = 0;
    printk( KERN_INFO "poll_dev:writing: %Ld\n",filp->f_version);

    while ( buf_pos == BUF_SIZ ) {
        if ( filp->f_flags & O_NONBLOCK ) {
            return -EAGAIN;
        }
        if ( wait_event_interruptible( write_q, ( buf_pos != BUF_SIZ ) ) )
            return -ERESTARTSYS;
    }

    if ( count > ( BUF_SIZ - buf_pos ) )
        copy_len = BUF_SIZ - buf_pos;
    else
        copy_len = count;

    if ( copy_from_user( msg + buf_pos, buf, copy_len ) ) {
        return -EFAULT;
    }
    *pos    += copy_len;
    buf_pos += copy_len;
    wake_up_interruptible( &read_q );
    return copy_len;
}

static unsigned int poll_poll(struct file* filp, poll_table* wait){
    unsigned int retmask = 0;

    printk( KERN_INFO "poll_dev:polling\n");
    poll_wait(filp, &read_q,  wait);
    poll_wait(filp, &write_q, wait);
    
    if ( buf_pos != 0 ) {
        retmask |= ( POLLIN  | POLLRDNORM );
    }
    
    if ( buf_pos != BUF_SIZ ) {
        retmask |= ( POLLOUT | POLLWRNORM );
    }
    return retmask;
}

static struct file_operations poll_fops = {
  .owner   = THIS_MODULE,
  .read    = poll_read,
  .write   = poll_write,
  .open    = poll_open,
  .release = poll_release,
  .poll    = poll_poll,
};

int init_module( void ){
    if(register_chrdev( MAJOR_ID, "poll_dev", &poll_fops)){
        printk( KERN_INFO "poll_dev: init error\n" );
        return -EBUSY;
    }
    init_waitqueue_head( &write_q );
    init_waitqueue_head( &read_q );
    printk( KERN_INFO "poll_dev:init\n" );
    return 0;
}

void cleanup_module( void ){
    printk( KERN_INFO "poll_dev:cleanup\n");
    unregister_chrdev( MAJOR_ID, "poll_dev" );
}


