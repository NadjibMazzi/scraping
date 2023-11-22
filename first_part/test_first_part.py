from first_part.src import exercise_one, is_colorful_number, calculate, find_anagrams

test_output = "1\n2\nThree\n4\nFive\nThree\n7\n8\nThree\nFive\n11\nThree\n13\n14\nThreeFive\n16\n17\nThree\n19\nFive\nThree\n22\n23\nThree\nFive\n26\nThree\n28\n29\nThreeFive\n31\n32\nThree\n34\nFive\nThree\n37\n38\nThree\nFive\n41\nThree\n43\n44\nThreeFive\n46\n47\nThree\n49\nFive\nThree\n52\n53\nThree\nFive\n56\nThree\n58\n59\nThreeFive\n61\n62\nThree\n64\nFive\nThree\n67\n68\nThree\nFive\n71\nThree\n73\n74\nThreeFive\n76\n77\nThree\n79\nFive\nThree\n82\n83\nThree\nFive\n86\nThree\n88\n89\nThreeFive\n91\n92\nThree\n94\nFive\nThree\n97\n98\nThree\nFive\n"


def test_first_exercise(capsys):
    exercise_one()
    captured = capsys.readouterr()
    assert captured.out == test_output

test_output1 = "True\nFalse\nFalse\n"
def test_secend_exercise(capsys):
    print(is_colorful_number(263))   # Output: True
    print(is_colorful_number(236))   # Output: False
    print(is_colorful_number(2532))  # Output: False
    captured = capsys.readouterr()
    assert captured.out == test_output1

test_output2 = "5\nFalse\n9\nFalse\n"
def test_third_exercise(capsys):
    print(calculate(['4', '3', '-2']))  # Output: 5
    print(calculate(453))  # Output: False
    print(calculate(['nothing', 3, '8', 2, '1']))  # Output: 9
    print(calculate('54'))  # Output: False
    captured = capsys.readouterr()
    assert captured.out == test_output2

test_output3 = "['aabb', 'bbaa']\n['carer', 'racer']\n[]\n"
def test_fourth_exercise(capsys):
    print(find_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
    # Output: ['aabb', 'bbaa']

    print(find_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
    # Output: ['carer', 'racer']

    print(find_anagrams('laser', ['lazing', 'lazy', 'lacer']))
    # Output: []
    captured = capsys.readouterr()
    assert captured.out == test_output3
