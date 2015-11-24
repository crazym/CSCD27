#include <stdio.h>
int main () {
  int auth=0;  /* set by an authentication helper-function, not shown here */
  char name[50];  /* student name */
  char mark[5];  /* student mark (% out of 100, up to 2 decimal digits) */
  char rubric[128];  /* rubric comment(s) (semicolon ";" separated) */

  puts("Name?");
  gets(name);
  puts("Mark?");
  gets(mark);
  puts("Rubric Comments?");
  gets(rubric);

  if (auth == 13372) {  /* leetz */
    FILE *fp;
    fp = fopen("/courses/courses/cscd27f15/rosselet/asn/a3/marks/marks.html", "a");
    fprintf (fp, "<tr><td>%.50s</td><td>%s</td><td>%s</td></tr>\n", name, mark, rubric);
    close (fp);

    printf ("Successfully updated mark for student: %.50s (mark: %s) \n", name, mark);
  } else {
    printf ("Unauthorized access to markus!  This incident will be reported with IP address and data submitted:  (name: %.50s, mark: %s) \n", name, mark);
  };
  return 0;
}
