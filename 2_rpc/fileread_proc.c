#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <rpc/rpc.h>
#include <errno.h>
#include "fileread.h"

filechunk *read_1_svc(readargs *args, struct svc_req *req) {
		static filechunk retchunk;
		int fp;

		retchunk.len = -1;


		if ((fp = open(args->filename, O_RDONLY)) == -1) {
				return &retchunk;
		}

		/* assert: file is open */

		if (lseek(fp, args->offset, SEEK_SET) == -1) {
				return &retchunk;
		}

		retchunk.len = read(fp, retchunk.buf, args->len);
		retchunk.buf[retchunk.len] = '\0';


		close(fp);

		return &retchunk;
}

