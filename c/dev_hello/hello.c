#include <linux/kernel.h>
#include <linux/module.h>
#include <linux/fs.h>

MODULE_AUTHOR("tanarky");
MODULE_DESCRIPTION("\"hello world\" MODULE");
MODULE_LICENSE("GPL");

#define MAJOR_ID  280

static struct file_operations hello_fops = {
  owner : THIS_MODULE,
};

int init_module( void ){
    // キャラクタデバイス(MAJOR_ID=280番)として登録する
    if(register_chrdev( MAJOR_ID, "hello_dev", &hello_fops)){
        printk( KERN_INFO "hello_dev: init error\n" );
        return -EBUSY;
    }
    printk(KERN_INFO "hello_dev:init\n");
    return 0;
}

void cleanup_module( void ){
    printk(KERN_INFO "hello_dev:cleanup\n");
    // hello_devキャラクタデバイスを削除する
    unregister_chrdev( MAJOR_ID, "hello_dev" );
}


