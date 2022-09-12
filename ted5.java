
    /* - Grupo:
    - George Marques
    - Bruno Giuseppe
    - Cleber Rockemback
    - Marcelo Victor
    - Gustavo Azevedo
 */

    public class ExercicioJava {
        public static void main(String[] args) {
            int i = 1;
            while(i<=20){
                System.out.print(i);
                i++;
                if(i%5 == 0){
                    System.out.println();
                } else{
                    System.out.print('\t');
                }
            }
        }
    }