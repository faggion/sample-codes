#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/errno.h>
#include <linux/fs.h>
#include <asm/uaccess.h>
#include <linux/random.h>
#include <linux/slab.h>
#include <linux/time.h>

// Need for global variable "current"
#include <linux/sched.h>

//#include <linux/spinlock.h>
//static spinlock_t global_lock = SPIN_LOCK_UNLOCKED;
static int dummy_lock = 0;

MODULE_AUTHOR("PSI");
MODULE_DESCRIPTION("\"lock world\" MODULE");
MODULE_LICENSE("GPL");

static int lock_open( struct inode* inode, struct file* filp ){
    pid_t pid = current->pid;
    printk( KERN_INFO "lock_dev:open: current_pid=%ld, major=%d, minor=%d\n",
            pid,
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev));
    return 0;
}

static int lock_close( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "lock_dev:release pid=%ld\n", current->pid);
    return 0;
}

static ssize_t lock_read( struct file* filp, char* buf, size_t count, loff_t* pos ){
    char msg[] = "lock world\n";
    printk( KERN_INFO "lock_dev:reading: %s = %d\n", msg, sizeof(msg) );
    //copy_to_user(buf, msg, sizeof(msg));
    return count;
}

static ssize_t lock_write(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    pid_t pid = current->pid;

    printk( KERN_INFO "lock_dev:dummy_lock=%d, pid=%ld\n", dummy_lock, pid );
    dummy_lock++;

    //// 以下はOSが固まるので危険
    //long i=0;
    //printk( KERN_INFO "lock_dev:write start. locking...\n" );
    //spin_lock(&global_lock);
    //printk( KERN_INFO "lock_dev:lock success. waiting...\n" );
    //for(i=0;i<1000000;i++){
    //    printk( KERN_INFO "loop...\n" );
    //}
    //printk( KERN_INFO "lock_dev:wait finished. unlocking...\n" );
    //spin_unlock(&global_lock);
    //printk( KERN_INFO "lock_dev:unlocked. end.\n" );
    return count;
}

static ssize_t lock_poll(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    printk( KERN_INFO "lock_dev:polling\n" );
    return count;
}

static struct file_operations lock_fops = {
  owner   : THIS_MODULE,
  read    : lock_read,
  write   : lock_write,
  open    : lock_open,
  release : lock_close,
  poll    : lock_poll,
};

int init_module( void ){
    if(register_chrdev( 0x0721, "lock_dev", &lock_fops)){
        printk( KERN_INFO "lock_dev: init error\n" );
        return -EBUSY;
    }
    printk( KERN_INFO "lock_dev:init\n" );
    return 0;
}

void cleanup_module( void ){
    unregister_chrdev( 0x0721, "lock_dev" );
    printk( KERN_INFO "lock_dev:cleanup");
}


