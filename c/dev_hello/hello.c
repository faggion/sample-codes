#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/errno.h>
#include <linux/fs.h>
#include <asm/uaccess.h>
#include <linux/random.h>
#include <linux/slab.h>

MODULE_AUTHOR("PSI");
MODULE_DESCRIPTION("\"hello world\" MODULE");
MODULE_LICENSE("GPL");

static int hello_open( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "hello_dev:open\n" );
    return 0;
}

//fclose
static int hello_release( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "hello_dev:release\n");
    return 0;
}

//fread
static ssize_t hello_read( struct file* filp, char* buf, size_t count, loff_t* pos ){
    char msg[] = "hello world\n";
    printk( KERN_INFO "hello_dev:reading: %s = %d\n", msg, sizeof(msg) );
    copy_to_user(buf, msg, sizeof(msg));
    return count;
}

//fwrite
static ssize_t hello_write(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    printk( KERN_INFO "hello_dev:writing\n" );
    return count;
}

static struct file_operations hello_fops = {
  owner   : THIS_MODULE,
  read    : hello_read,
  write   : hello_write,
  open    : hello_open,
  release : hello_release,
};

int init_module( void ){
    if(register_chrdev( 0x0721, "hello_dev", &hello_fops)){
        printk( KERN_INFO "hello_dev: init error\n" );
        return -EBUSY;
    }
    printk( KERN_INFO "hello_dev:init\n" );
    return 0;
}

void cleanup_module( void ){
    unregister_chrdev( 0x0721, "hello_dev" );
    printk( KERN_INFO "hello_dev:cleanup");
}


