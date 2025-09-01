echo "Start maze 02 searching tests...\n"

uv run main.py --file examples/maze02.txt --alg dfs --wire 10
uv run main.py --file examples/maze02.txt --alg a_star --wire 8

echo "\n\nStart maze 03 searching tests...\n"

uv run main.py --file examples/maze03.txt --alg dfs --wire 11
uv run main.py --file examples/maze03.txt --alg a_star --wire 6

echo "\n\nStart maze 04 searching tests...\n"

uv run main.py --file examples/maze04.txt --alg dfs --wire 5
uv run main.py --file examples/maze04.txt --alg a_star --wire 6

echo "\n\nStart maze 05 searching tests...\n"

uv run main.py --file examples/maze05.txt --alg dfs --wire 11
uv run main.py --file examples/maze05.txt --alg a_star --wire 4

echo "\n\nStart maze 06 searching tests...\n"

uv run main.py --file examples/maze06.txt --alg dfs --wire 1
uv run main.py --file examples/maze06.txt --alg a_star --wire 1
