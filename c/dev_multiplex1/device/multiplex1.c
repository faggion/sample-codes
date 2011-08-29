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
MODULE_DESCRIPTION("test multiplex1 MODULE");
MODULE_LICENSE("GPL");

#define MAJOR_ID 280
#define NDEV 4

static struct {
    int status;
    wait_queue_head_t wait;
} device[NDEV];

static int multiplex1_open( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "multiplex1_dev:open: pid=%d, major=%d, minor=%d\n",
            current->pid,
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev));
    return 0;
}

static int multiplex1_release( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "multiplex1_dev:release: pid=%d, major=%d, minor=%d\n",
            current->pid,
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev));
    return 0;
}

// server/client両方から呼ばれる可能性があるのでminorを見て処理の場合分け
static ssize_t multiplex1_read(struct file* filp, char* buf, size_t count, loff_t* pos ){
    struct inode *inode = filp->f_dentry->d_inode;
    int minor = MINOR(inode->i_rdev);

    printk( KERN_INFO "multiplex1_dev:read(%d): pid=%d, major=%d\n",
            minor,
            current->pid,
            MAJOR(inode->i_rdev));

    if(NDEV <= minor){
        return count;
    }

    // server用device すなわち server側からrequestをreadした場合
    if(minor % 2 == 0){
        device[minor].status = -1; // server側の処理が終わったので-1にする
        //wake_up_interruptible( &device[minor].wait );
        wake_up( &device[minor].wait );
    }
    // client用device
    else{
        // 単方向通信なので、空実装
    }
    return count;
}

// server/client両方から呼ばれる可能性があるのでminorを見て処理の場合分け
static ssize_t multiplex1_write(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    struct inode *inode = filp->f_dentry->d_inode;
    int minor = MINOR(inode->i_rdev);

    printk( KERN_INFO "multiplex1_dev:write(%d): pid=%d, major=%d\n",
            minor,
            current->pid,
            MAJOR(inode->i_rdev));

    if(NDEV <= minor){
        return count;
    }

    // server用device
    if(minor % 2 == 0){
        // 単方向通信なので、空実装
    }
    // client用device すなわち client側からrequestをwriteした場合
    else{
        device[minor-1].status = 1; // server側をreadableに
        printk(KERN_INFO "multiplex1_dev:write(%d -> %d): req[server]: %d\n",
               minor,
               minor-1,
               device[minor-1].status);
        //wake_up_interruptible( &device[minor-1].wait );
        wake_up( &device[minor-1].wait );
    }
    return count;
}

// ここは必ずserverからしか呼び出されない
static unsigned int multiplex1_poll(struct file* filp, poll_table* wait){
    unsigned int retmask = 0;
    struct inode *inode = filp->f_dentry->d_inode;
    int minor = MINOR(inode->i_rdev);

    printk( KERN_INFO "multiplex1_dev:poll(%d): pid=%d, major=%d\n",
            minor,
            current->pid,
            MAJOR(inode->i_rdev));

    if(NDEV <= minor){
        return 0;
    }

    poll_wait(filp, &device[minor].wait,  wait);
    
    printk(KERN_INFO "multiplex1_dev:poll(%d): req = %d\n", minor, device[minor].status);

    if (0 < device[minor].status){
        printk( KERN_INFO "multiplex1_dev:poll(%d): readable request[%d]\n", minor, device[minor].status);
        retmask |= ( POLLIN  | POLLRDNORM );
    }
    if (device[minor].status < 0){
        printk( KERN_INFO "multiplex1_dev:poll(%d): empty request. now, writable\n", minor);
        retmask |= ( POLLOUT | POLLWRNORM );
    }
    return retmask;
}

static struct file_operations multiplex1_fops = {
  .owner   = THIS_MODULE,
  .read    = multiplex1_read,
  .write   = multiplex1_write,
  .open    = multiplex1_open,
  .release = multiplex1_release,
  .poll    = multiplex1_poll,
};

int init_module( void ){
    int i;
    if(register_chrdev( MAJOR_ID, "multiplex1_dev", &multiplex1_fops)){
        printk( KERN_INFO "multiplex1_dev: init error\n" );
        return -EBUSY;
    }
    for(i=0;i<NDEV;i++){
        printk( KERN_INFO "multiplex1_dev:initialize %d\n", i);
        device[i].status = -1;
        init_waitqueue_head( &device[i].wait );
    }
    printk( KERN_INFO "multiplex1_dev:init\n" );
    return 0;
}

void cleanup_module( void ){
    printk( KERN_INFO "multiplex1_dev:cleanup\n");
    unregister_chrdev( MAJOR_ID, "multiplex1_dev" );
}
