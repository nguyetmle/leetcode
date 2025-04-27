/**
    Given an integer numRows, return the first numRows of Pascal's triangle.
 */

//level: easy

class PascalTriangle {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> allRows = new ArrayList<>();

        //create each row of the triangle and add to allRows
        for (int i=0; i<numsRows; i++) {
            Integer[] row = new Integer[i+1]; 
            Arrays.fill(row,1); //temporarily fill row with 1
            allRows.add(Arrays.asList(row));
        }

        //loop through each row, starting from the second row
        for (int i=2; i<numRows; i++) {
            //loop through each number in a row, starting from the second till the one before the last number
            for (int j=1; j<allRows.get(i).size()-1; j++) {
                //change number in each row in acccordance to Pascal rule
                allRows.get(i).set(j, allRows.get(i-1).get(j-1) + allRows.get(i-1).get(j));
            }
        }

        return allRows;
    }
}