#pragma once
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::unordered_map<int, int> num2i;
        num2i.reserve(nums.size());

        for (int i = 0; i < nums.size(); ++i) {
            auto seen_it = num2i.find(target - nums[i]);
            if (seen_it != num2i.end()) {
                return {seen_it->second, i};
            }

            num2i[nums[i]] = i;
        }

        return {};
    }
};
