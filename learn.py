# Copyright 2024 ninad
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     https://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import random
def get_random_number():
    return random.randint(0,100)
def input_number(x):
    while True:
        try :
            return int(x)
        except ValueError:
            print("ValueError")
def main():
    x=get_random_number()
    print(input_number(x))
    print(x & 1 == 0)
    dice=[1,2,3,4,5,6]
    roll_dice=random.choice(dice)
    print(roll_dice)

if __name__=="__main__":
    main()
