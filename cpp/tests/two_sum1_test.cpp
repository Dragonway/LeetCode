#include <catch2/catch_test_macros.hpp>
#include <catch2/generators/catch_generators.hpp>
#include <catch2/matchers/catch_matchers_vector.hpp>
#include "two_sum1.hpp"

TEST_CASE("two_sum1") {
    auto [nums, target, expected] = GENERATE(table<std::vector<int>, int, std::vector<int>>({
        {{2, 7, 11, 15},    9,  {0, 1}},
        {{3, 2, 4},         6,  {1, 2}},
        {{-1, 0, 9, -5},    -6, {0, 3}},
        {{0, 0},            0,  {0, 1}},
    }));

    CAPTURE(nums, target);
    Solution s;
    REQUIRE_THAT(s.twoSum(nums, target), Catch::Matchers::UnorderedEquals(expected));
}
