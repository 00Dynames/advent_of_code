package day2;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class DayTwo {

    public static void main(String[] args) throws IOException {

//        List<String> input = Files.readAllLines(Paths.get("2021/inputs/day2small.txt"));
        List<String> input = Files.readAllLines(Paths.get("2021/inputs/day2large.txt"));

        System.out.println(path(input));
    }

    private static int path(List<String> instructions){

        int depth = 0;
        int horizontal = 0;

        for(String instruction:instructions){
            List<String> s = List.of(instruction.split(" "));
            if(s.get(0).equals("forward")){
                horizontal += Integer.parseInt(s.get(1));
            } else if (s.get(0).equals("down")){
                depth += Integer.parseInt(s.get(1));
            } else if (s.get(0).equals("up")){
                depth -= Integer.parseInt(s.get(1));
            }
        }

        return depth * horizontal;
    }

    private static int aimedPath(List<String> instructions){
        return -1;
    }

}
