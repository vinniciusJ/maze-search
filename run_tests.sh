# uv run main.py --file examples/maze00.txt --alg greedy
# uv run main.py --file examples/maze00.txt --alg a_star
# uv run main.py --file examples/maze00.txt --alg a_star_wire --wire 7

# uv run main.py --file examples/maze01.txt --alg greedy
# uv run main.py --file examples/maze01.txt --alg a_star
# uv run main.py --file examples/maze01.txt --alg a_star_wire --wire 7
echo "Start maze 02 searching tests...\n"

uv run main.py --file examples/maze02.txt --alg greedy --wire 10
uv run main.py --file examples/maze02.txt --alg a_star --wire 8

echo "\n\nStart maze 03 searching tests...\n"

uv run main.py --file examples/maze03.txt --alg greedy --wire 11
uv run main.py --file examples/maze03.txt --alg a_star --wire 6

echo "\n\nStart maze 04 searching tests...\n"

uv run main.py --file examples/maze04.txt --alg greedy --wire 5
uv run main.py --file examples/maze04.txt --alg a_star --wire 6

echo "\n\nStart maze 05 searching tests...\n"

uv run main.py --file examples/maze05.txt --alg greedy --wire 11
uv run main.py --file examples/maze05.txt --alg a_star --wire 4

echo "\n\nStart maze 06 searching tests...\n"

uv run main.py --file examples/maze06.txt --alg greedy --wire 1
uv run main.py --file examples/maze06.txt --alg a_star --wire 1
