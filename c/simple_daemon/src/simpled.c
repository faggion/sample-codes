#include <sys/types.h>
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>
#include <errno.h>
#include <stdlib.h>
#include <signal.h>
#include <string.h>
#include <pthread.h>

#define UNUSED(x) ((void)(x))

static sigset_t dfl_set;
static sigset_t sig_set;
static int main_rc = EXIT_SUCCESS;
static int shutdown_flg = 0;

void usage(const char *myname){
    fprintf(stderr, "usage: %s proc_name\n", myname);
}

static void handle_signals(void){
    struct timespec timeout;
    int ret;

    timeout.tv_sec = 0;
    timeout.tv_nsec = 0;
    while((ret = sigtimedwait(&sig_set, NULL, &timeout) ) > 0 ){
        if( SIGCHLD == ret || SIGPIPE == ret ){
            fprintf(stderr, "got CHLD or PIPE\n");
            continue;
        }
        fprintf(stderr, "got sig %d, %d, %d\n", ret, SIGCHLD, SIGPIPE);

        shutdown_flg = 1;
        main_rc = EXIT_FAILURE;
        break;
    }
    return;
}

static int mainloop(void){
    sigfillset(&sig_set);
    pthread_sigmask(SIG_BLOCK, &sig_set, &dfl_set);

    while(!shutdown_flg){
        //cmdport_handle();
        if(shutdown_flg) break;
        handle_signals();
    }
    return(1);
}

int main(int argc, const char **argv){

    if(argc != 2){
        usage(argv[0]);
        main_rc = EXIT_FAILURE;
        goto finally;
    }

    mainloop();

  finally:

    return(main_rc);
}

