#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/errno.h>
#include <linux/fs.h>
#include <asm/uaccess.h>
#include <linux/random.h>
#include <linux/slab.h>
#include <linux/time.h>


MODULE_AUTHOR("PSI");
MODULE_DESCRIPTION("\"write world\" MODULE");
MODULE_LICENSE("GPL");

static int write_open( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "write_dev:open: major=%d, minor=%d\n",
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev));
    return 0;
}

//fclose
static int write_release( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "write_dev:release\n");
    return 0;
}

//fread
static ssize_t write_read( struct file* filp, char* buf, size_t count, loff_t* pos ){
    char msg[] = "write world\n";
    printk( KERN_INFO "write_dev:reading: %s = %d\n", msg, sizeof(msg) );
    //copy_to_user(buf, msg, sizeof(msg));
    return count;
}

//fwrite
static ssize_t write_write(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    printk( KERN_INFO "write_dev:writing1\n" );
    DECLARE_WAIT_QUEUE_HEAD(wait);
    sleep_on_timeout(&wait, 250 * 5); // 250で1秒だった、なぜ？
    printk( KERN_INFO "write_dev:writing2\n" );
    return count;
}

//fwrite
static ssize_t write_poll(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    printk( KERN_INFO "write_dev:polling\n" );
    return count;
}

static struct file_operations write_fops = {
  owner   : THIS_MODULE,
  read    : write_read,
  write   : write_write,
  open    : write_open,
  release : write_release,
  poll    : write_poll,
};

int init_module( void ){
    if(register_chrdev( 0x0721, "write_dev", &write_fops)){
        printk( KERN_INFO "write_dev: init error\n" );
        return -EBUSY;
    }
    printk( KERN_INFO "write_dev:init\n" );
    return 0;
}

void cleanup_module( void ){
    unregister_chrdev( 0x0721, "write_dev" );
    printk( KERN_INFO "write_dev:cleanup");
}


