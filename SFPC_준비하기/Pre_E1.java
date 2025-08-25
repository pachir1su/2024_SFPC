import java.util.Comparator;
import java.util.Scanner;
import java.util.Arrays;
     class Main {
        public static void main (String[]args) {
            Scanner sc = new Scanner(System.in);

            int per = sc.nextInt();// 방문한 음식점의 개수
            int sticker_per = sc.nextInt();//받은 스티커의 개수
            int person[][] = new int[2][sticker_per];//사람당 받은 스티커 번호의 배열
            int sticker[] = new int[sticker_per * 2];

            for (int i = 0; i < sticker_per; i++) //첫번째 스티커를 정하는 경우의 수
            {
                person[0][i] = sc.nextInt();
                sticker[i] = person[0][i];
            }

            for (int i = 0; i < sticker_per; i++)//두번째 스티커를 정하는 경우의 수
            {
                person[1][i] = sc.nextInt();
                sticker[i + sticker_per] = person[1][i];
            }
            Arrays.sort(sticker);
            sticker = Arrays.stream(sticker).distinct().toArray();
            for (int i = 1; i <= per; i++)
                {
                    if(sticker[i-1] !=i)
                        {
                            System.out.println("NO");
                            System.exit(i);
                        } else if (sticker[i-1]==per) {
                        System.out.println("YES");
                    }

                }

        }
    }