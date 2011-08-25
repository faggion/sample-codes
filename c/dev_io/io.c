#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/errno.h>
#include <linux/fs.h>
// for copy_to_user/copy_from_user
#include <asm/uaccess.h>
// for ioctl
#include <linux/ioctl.h>
#include <linux/poll.h>
#include <linux/sched.h>
#include <linux/wait.h>
#include <linux/version.h>

#define WRITE_BUF_SIZ 64
#define MAJOR_ID 280

MODULE_AUTHOR("tanarky");
MODULE_DESCRIPTION("read write sample");
MODULE_LICENSE("GPL");

static int flag = 0;

static int io_open( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "io_dev:open: major=%d, minor=%d, flag=%d\n",
            MAJOR(inode->i_rdev),
            MINOR(inode->i_rdev),
            flag);
    return 0;
}

static int io_release( struct inode* inode, struct file* filp ){
    printk( KERN_INFO "io_dev:release\n");
    return 0;
}

static ssize_t io_read( struct file* filp, char* buf, size_t count, loff_t* pos ){
    char msg[] = "message from kernel to user\n";
    copy_to_user(buf, msg, sizeof(msg));
    return count;
}

static ssize_t io_write(struct file* filp,
                        const char* buf,
                        size_t count,
                        loff_t* pos ){
    char msg[WRITE_BUF_SIZ];
    // flagが立っていたら書き込みエラー
    if(flag){
        printk(KERN_INFO "io_dev:flag error %d\n", flag);
        return -EFAULT;
    }
    if(WRITE_BUF_SIZ <= count){
        printk(KERN_INFO "io_dev:too much data. max = %d\n", WRITE_BUF_SIZ - 1);
        return -EFAULT;
    }
    if( copy_from_user( msg, buf, count ) ){
        printk(KERN_INFO "copy_from_user failed\n");
        return -EFAULT;
    }
    msg[count] = '\0';
    printk(KERN_INFO "receiced message = %s", msg);
    printk(KERN_INFO "position = %d\n", (int)*pos);
    *pos += count; // 分割して読み込むときに必要っぽい
    return count;
}

//static ssize_t io_poll(struct file* filp, const char* buf, size_t count, loff_t* pos ){
//    printk(KERN_INFO "io_dev:polling\n");
//    return count;
//}

#if LINUX_VERSION_CODE < KERNEL_VERSION(2,6,36)
static int io_ioctl(struct inode* inode,struct file* filp,unsigned int cmd,unsigned long arg)
#else
static int io_ioctl(struct file* filp,unsigned int cmd,unsigned long arg)
#endif
{
    printk(KERN_INFO "io_dev:io_ctl\n");
    return 0;
}

//static struct file_operations io_fops = {
//  owner   : THIS_MODULE,
//  read    : io_read,
//  write   : io_write,
//  open    : io_open,
//  //poll    : io_poll,
//  ioctl   : io_ioctl,
//  release : io_release,
//};

static struct file_operations io_fops = {
  .read    = io_read,
  .write   = io_write,
  .open    = io_open,
#if LINUX_VERSION_CODE < KERNEL_VERSION(2,6,36)
  .ioctl   = io_ioctl,
#else
  .unlocked_ioctl   = io_ioctl,
#endif
  .release = io_release,
};

int init_module( void ){
    if(register_chrdev( MAJOR_ID, "io_dev", &io_fops)){
        printk(KERN_INFO "io_dev: init error\n");
        return -EBUSY;
    }
    printk(KERN_INFO "io_dev:init\n");
    return 0;
}

void cleanup_module( void ){
    printk(KERN_INFO "io_dev:cleanup\n");
    unregister_chrdev( MAJOR_ID, "io_dev" );
}


