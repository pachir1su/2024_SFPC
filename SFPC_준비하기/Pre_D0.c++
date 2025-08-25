#include <iostream>
#include <algorithm>
#include <cmath>

int main() {
    const int SOUP_PER_BOWL = 400;
    const int SUNDAY_PER_BOWL = 150;
    const int MEAT_PER_BOWL = 140;
    const int CHIVE_PER_BOWL = 23;

    int soup_day1 = 54300;
    int sunday_day1 = 13540;
    int meat_day1 = 13000;
    int chive_day1 = 1000;

    int soup_day2 = 93300;
    int sunday_day2 = 31540;
    int meat_day2 = 30000;
    int chive_day2 = 1000;

    int bowls_day1 = std::min({ soup_day1 / SOUP_PER_BOWL,
                               sunday_day1 / SUNDAY_PER_BOWL,
                               meat_day1 / MEAT_PER_BOWL,
                               chive_day1 / CHIVE_PER_BOWL });

    soup_day1 -= bowls_day1 * SOUP_PER_BOWL;
    sunday_day1 -= bowls_day1 * SUNDAY_PER_BOWL;
    meat_day1 -= bowls_day1 * MEAT_PER_BOWL;
    chive_day1 -= bowls_day1 * CHIVE_PER_BOWL;

    int total_soup_day2 = soup_day2 + soup_day1;
    int total_sunday_day2 = sunday_day2 + sunday_day1;
    int total_meat_day2 = meat_day2 + meat_day1;
    int total_chive_day2 = chive_day2 + chive_day1;

    int bowls_day2 = std::min({ total_soup_day2 / SOUP_PER_BOWL,
                               total_sunday_day2 / SUNDAY_PER_BOWL,
                               total_meat_day2 / MEAT_PER_BOWL,
                               total_chive_day2 / CHIVE_PER_BOWL });

    int total_bowls = bowls_day1 + bowls_day2;

    std::cout << total_bowls << std::endl;

    return 0;
}