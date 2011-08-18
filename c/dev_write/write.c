#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/errno.h>
#include <linux/fs.h>
// for copy_to_user/copy_from_user
#include <asm/uaccess.h>

#define WRITE_BUF_SIZ 64
#define MAJOR_ID 280

MODULE_AUTHOR("tanarky");
MODULE_DESCRIPTION("read write sample");
MODULE_LICENSE("GPL");

static int write_open( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "write_dev:open: major=%d, minor=%d\n",
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev));
    return 0;
}

static int write_release( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "write_dev:release\n");
    return 0;
}

static ssize_t write_read( struct file* filp, char* buf, size_t count, loff_t* pos ){
    char msg[] = "message from kernel to user\n";
    copy_to_user(buf, msg, sizeof(msg));
    return count;
}

static ssize_t write_write(struct file* filp,
                           const char* buf,
                           size_t count,
                           loff_t* pos ){
    char msg[WRITE_BUF_SIZ];
    if(WRITE_BUF_SIZ <= count){
        printk(KERN_INFO "write_dev:too much data. max = %d\n", WRITE_BUF_SIZ - 1);
        return -EFAULT;
    }
    if( copy_from_user( msg, buf, count ) ){
        printk(KERN_INFO "copy_from_user failed\n");
        return -EFAULT;
    }
    msg[count] = '\0';
    printk(KERN_INFO "receiced message = %s", msg);
    *pos += count; // 分割して読み込むときに必要っぽい
    return count;
}

static ssize_t write_poll(struct file* filp, const char* buf, size_t count, loff_t* pos ){
    printk(KERN_INFO "write_dev:polling\n");
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
    if(register_chrdev( MAJOR_ID, "write_dev", &write_fops)){
        printk(KERN_INFO "write_dev: init error\n");
        return -EBUSY;
    }
    printk(KERN_INFO "write_dev:init\n");
    return 0;
}

void cleanup_module( void ){
    printk(KERN_INFO "write_dev:cleanup\n");
    unregister_chrdev( MAJOR_ID, "write_dev" );
}


