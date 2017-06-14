/**
 * Created by af on 2017-06-14.
 */

var cell_list = document.getElementById("cell_list");
var i;

for(i = 0; i < cell_list.length; i++) {
    if ( i % 3 == 0 ) {
        document.write("<tr>\n");
    }
    document.write("<td>\n"+cell_list+"\n<td>\n");
    if ( i % 3 == 0 ) {
        document.write("\n</tr>\n");
    }
}