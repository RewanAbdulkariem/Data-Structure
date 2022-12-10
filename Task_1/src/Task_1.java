import java.util.*;

interface calculator{
        /**
    * Adds given two numbers
    * @param x first number
    * @param y second number
    * @return the sum of the two numbers
    */
    int add(int x, int y);
    /**
    * Divides two numbers
    * @param x first number
    * @param y second number
    * @return the division result
    */
    float divide(int x, int y) throws RuntimeException;
    
    
}
class Icalculator implements calculator{
    @Override
    public int add(int x,int y){
        int sum = x +y;
        return sum;
    }
    @Override
    public float divide(int x, int y)throws RuntimeException{
        float division = (float)x / y;
        return division;
    }
    
}


public class Task_1 {

    public static void main(String[] args) {
        
        Icalculator cal = new Icalculator();
        
        Scanner input = new Scanner(System.in);
            int number1 = input.nextInt();
            char op = input.next().charAt(0);
            int number2 = input.nextInt();
            if (op == '+')
            {
               int result = cal.add(number1, number2);
              System.out.println(result);
            }
            else if (op == '/')
            {
               float result = cal.divide(number1, number2);
                if (number2==0)
                {
                    System.out.println("Error");
                }
                else
                {
                    System.out.println(result);
                }
            
        }
    }
}
