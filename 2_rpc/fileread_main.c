#include <stdio.h>
#include <stdlib.h>
#include "fileread.h"

int main(int argc, char *argv[]) {
		
		CLIENT *clnt;
		filechunk *chunk;
		readargs args;
		unsigned int len;

		if (argc != 3) {
				fprintf(stderr, "usage: ./client <server> <file>\n");
				return 0;
		}

		strcpy(args.filename, argv[2]);
		args.offset = 0;
		args.len = 4096;

		if ((clnt = clnt_create(argv[1], FILEPROG, FILEPROGVER, "tcp")) == NULL) {
				clnt_pcreateerror(argv[1]);
				exit(1);
		}
		
		do {
				chunk = read_1(&args, clnt);
				chunk->buf[chunk->len] = '\0';

				printf("%s", chunk->buf);
				args.offset += chunk->len;

				len = chunk->len;


		}while(len);



		return 0;
}


