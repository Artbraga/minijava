// test comment one line 1
class Factorial{
    // test comment one line 2
    // test comment one line 2
    public static void main(String[] a){
	System.out.println(new Fac().ComputeFac(10));
    }
}

/* test comment multiple lines 1 */
class Fac {

}
/* test comment multiple
    lines 2
*/
    public int ComputeFac(int num){
	int num_aux ;
	if (num < 1)
	    num_aux = 1 ;
	else
	    num_aux = num * (this.ComputeFac(num-1)) ;
	return num_aux ;
    }
}