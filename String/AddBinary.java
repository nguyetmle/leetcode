/**
    Given two binary strings a and b, return their sum as a binary string.
*/

//level: easy
//approach: start from the last characters of 2 strings and compute 
//          the digit sum one by one. if sum>1, store carry for the next digits

class AddBinary {
    public String addBinary(String a, String b) {
        if (a=="")
            return b;
        if (b=="")
            return a;

        //use StringBuilder (mutable) for string manipulation instead of String (immutable)
        StringBuilder sb = new StringBuilder();

        int i = a.length()-1;
        int j = b.length()-1;
        int carry=0;

        //traverse 2 string from the end
        while (i>=0 || j>=0) {
            int sum = carry; //if there is a carry from the last addition, add it to sum
            //compute sum of each digit
            if (i>=0)
                sum += a.charAt(i) - '0'; //subtract '0' to get the int value of char from the ascii
            if (j>=0)
                sum += b.charAt(j) - '0';
            
            //since a and b are binary numbers (0 & 1), the sum of each digit can be 0, 1 or 2. 
            //if sum==2 or summ==0, append 0 to result string
            //if sum==1, append 1 to result string
            sb.append(sum%2);

            //if sum==2, we have a carry of 1
            //else, no carry bc 1/2 rounds down to 0
            carry = sum/2;

            i--;
            j--;
        }

        //leftover carry, add it
        if (carry != 0)
            sb.append(carry);

        return sb.reverse().toString();

    }
}