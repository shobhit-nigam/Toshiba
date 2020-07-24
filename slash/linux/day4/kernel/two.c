#include<linux/module.h>
#include<linux/kernel.h>
#include<linux/init.h>

//executes during loading of module into the kernel
static int __init batman_init(void)
{
	printk(KERN_INFO "batman begins\n");
	printk(KERN_INFO "module uploaded in Gotham city\n");
	return 0;
}

void __exit batman_exit(void)
{
	printk(KERN_INFO "Joker ends\n-------\n");
}

module_init(batman_init);
module_exit(batman_exit);

MODULE_LICENSE("toshiba software");
MODULE_AUTHOR("christopher nolan");
MODULE_DESCRIPTION("simple module");
MODULE_VERSION("3.1.1");

