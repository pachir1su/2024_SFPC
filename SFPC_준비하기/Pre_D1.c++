#include <stdio.h>
int main(){
   long long a, b, c, d;
   long long fa, fb, fc, fd;
   long long sa, sb, sc, sd;
   int score=0;
   scanf("%lld %lld %lld %lld", &a, &b, &c, &d);
   scanf("%lld %lld %lld %lld", &fa, &fb, &fc, &fd);
   scanf("%lld %lld %lld %lld", &sa, &sb, &sc, &sd);
   
      for(int i=0;i<10000;i++){
             fa-=a;
            fb-=b;
            fc-=c;
            fd-=d;
         if(fa>=0&&fb>=0&&fc>=0&&fd>=0){
            
            score+=1;
         }
         else{
            break;
         }
      }
      if(fd<0){
         sd+=fd+=d;
      }
      else{
         sd+=fd;
      }
       
      for(int i=0;i<10000;i++){
            sa-=a;
            sb-=b;
            sc-=c;
            sd-=d;
         if(sa>=0&&sb>=0&&sc>=0&&sd>=0){
         
            score+=1;
         }
         else{
            break;
         }
      }
   
   printf("%d", score);

   return 0;
}