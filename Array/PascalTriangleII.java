/**
    Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
*/

//level: easy
//approach: - each element of nth row in pascal's triangle can be represented as nCi, where i is the ith element in the row
//          - nCi = n! / (i! * (n-i)!)
//          - nC(i-1) = n! / ((i-1)! * (n-(i-1))!)
//         => nCi / nC(i-1) = ((i-1)! * (n-i+1))!) / (i! * (n-i)!)
//         => nCi = nC(i-1) * (n-i+1)/i


class PascalTriangleII {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> res = new ArrayList<>();

        //add 1 as first element of row
        res.add(1);

        for (int i=1; i<=rowIndex; i++) {
            res.add(i, (res.get(i-1) * (rowIndex-i+1)/i));
        }

        return res;
    }
}