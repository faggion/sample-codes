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
MODULE_DESCRIPTION("test simplex MODULE");
MODULE_LICENSE("GPL");

#define MAJOR_ID 280

static int req = -1;
static wait_queue_head_t server_q;

static int simplex_open( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "simplex_dev:open: pid=%d, major=%d, minor=%d\n",
            current->pid,
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev));
    return 0;
}

static int simplex_release( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "simplex_dev:release: pid=%d, major=%d, minor=%d\n",
            current->pid,
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev));
    return 0;
}

// server/client両方から呼ばれる可能性があるのでminorを見て処理の場合分け
static ssize_t simplex_read(struct file* filp, char* buf, size_t count, loff_t* pos ){
    struct inode *inode = filp->f_dentry->d_inode;
    int minor = MINOR(inode->i_rdev);

    printk( KERN_INFO "simplex_dev:read(%d): pid=%d, major=%d\n",
            minor,
            current->pid,
            MAJOR(inode->i_rdev));

    // server用device すなわち server側からrequestをreadした場合
    if(minor == 0){
        if(copy_to_user(buf, (void *)&req, sizeof(int))){
            return -EFAULT;
        }
        req = -1;
        wake_up_interruptible( &server_q );
    }
    // client用device
    else{
        // 単方向通信なので、空実装
    }
    return count;
}

// server/client両方から呼ばれる可能性があるのでminorを見て処理の場合分け
static ssize_t simplex_write(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    struct inode *inode = filp->f_dentry->d_inode;
    int minor = MINOR(inode->i_rdev);

    printk( KERN_INFO "simplex_dev:write(%d): pid=%d, major=%d\n",
            minor,
            current->pid,
            MAJOR(inode->i_rdev));

    // server用device
    if(minor == 0){
        // 単方向通信なので、空実装
    }
    // client用device すなわち client側からrequestをwriteした場合
    else{
        if(copy_from_user((void *)&req, buf, sizeof(int))){
            return -EFAULT;
        }
        printk(KERN_INFO "simplex_dev:write(%d): received: %d\n", minor, req);
        wake_up_interruptible( &server_q );
    }
    return count;
}

// ここは必ずserverからしか呼び出されない
static unsigned int simplex_poll(struct file* filp, poll_table* wait){
    unsigned int retmask = 0;
    struct inode *inode = filp->f_dentry->d_inode;
    int minor = MINOR(inode->i_rdev);

    printk( KERN_INFO "simplex_dev:poll(%d): pid=%d, major=%d\n",
            minor,
            current->pid,
            MAJOR(inode->i_rdev));

    poll_wait(filp, &server_q,  wait);
    
    printk(KERN_INFO "simplex_dev:poll(%d): req = %d\n", minor, req);

    if (0 < req){
        printk( KERN_INFO "simplex_dev:poll(%d): readable request[%d]\n", minor, req);
        retmask |= ( POLLIN  | POLLRDNORM );
    }
    if (req < 0){
        printk( KERN_INFO "simplex_dev:poll(%d): empty request. now, writable\n", minor);
        retmask |= ( POLLOUT | POLLWRNORM );
    }
    return retmask;
}

static struct file_operations simplex_fops = {
  .owner   = THIS_MODULE,
  .read    = simplex_read,
  .write   = simplex_write,
  .open    = simplex_open,
  .release = simplex_release,
  .poll    = simplex_poll,
};

int init_module( void ){
    if(register_chrdev( MAJOR_ID, "simplex_dev", &simplex_fops)){
        printk( KERN_INFO "simplex_dev: init error\n" );
        return -EBUSY;
    }
    init_waitqueue_head( &server_q );
    printk( KERN_INFO "simplex_dev:init\n" );
    return 0;
}

void cleanup_module( void ){
    printk( KERN_INFO "simplex_dev:cleanup\n");
    unregister_chrdev( MAJOR_ID, "simplex_dev" );
}
