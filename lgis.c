#include <stdio.h>
#include <stdlib.h>

int *lgst_sbsq(int *seq);

int main(int argc, char *argv[])
{
    int i, len, *num_list;
    size_t maxlen = 10;
    FILE *fp;
    char *filename;
    char *line = malloc(maxlen * 8);
    filename = argc > 1 ? argv[1] : "rosalind_lgis.txt";
    if ((fp = fopen(filename, "r")) == NULL) {
        fprintf(stderr, "Error: could not open %s.\n", filename);
        return -1;
    }
    fscanf(fp, "%d", &len);
    num_list = malloc(sizeof(int) * len);
    for (i = 0; i < len; i++) {
        fscanf(fp, "%d", &(num_list[i]));
        printf("%d\n", num_list[i]);
    }
}

int *lgst_sbsq(int *seq)
{
    int len = seq[0];
    int *lgst_subseq;
    int *subseq;
    int i, j;

    if (len == 1)
        return seq;
    /* allocate enough space */
    lgst_subseq = malloc((sizeof(int) + 1)* len);
    subseq = malloc((sizeof(int) + 1)* len);
    /* first int indicates the length */
    lgst_subseq[0] = subseq[0] = 0;

    for (i = 1; i <= len; i++) {
        /* empty subseq */
        subseq[0] = 1;
        subseq[1] = seq[i];







        
