#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

int main()
{
    std::ifstream calFile;
    calFile.open("input.txt");

    std::string sbuffer;
    std::vector<int> array = {};
    int elfCals = 0;


    if (calFile.is_open()) {
         while (calFile) {
            std::getline (calFile, sbuffer);
            if (sbuffer.empty() == false){
                elfCals = elfCals + stoi(sbuffer);
            } else if (sbuffer.empty()) {
                array.push_back(elfCals);
                elfCals = 0;
                continue;

            }
            
         }
         int max = *std::max_element(array.begin(), array.end());

         std::cout << "Max value: " << max << std::endl;
    }
    return 0;
}