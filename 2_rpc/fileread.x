const MAXBUFLEN = 4096;
const MAXNAMELEN = 256;

struct filechunk {
	char buf[MAXBUFLEN]; /* data */
	unsigned int len;    /* length of data */
};

struct readargs {
	char filename[MAXNAMELEN];      /* name of file to be read */
	unsigned int offset; 			/* position (bytes) where chunk starts */
	unsigned int len;    			/* number of bytes requested */
};
	

program FILEPROG {
	version FILEPROGVER {
		filechunk READ(readargs) = 1;
	} = 1;
} = 0x20000000;
