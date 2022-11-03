import traceback
from converter import *


while True:
    pc = PostfixConverter()

    try:
        question = input("\n\nInput question (Ctrl+D to stop): ")
        ops = input("\n\nInput equation (Ctrl+D to stop): ")

        result, code_string = pc.convert(ops, question)

        print("\n=== Code String ===", code_string, sep='\n')
        print("\n=== Execution ===")
        exec(code_string)
        print("\n=== Result ===", result, sep='\n')
    
    except (EOFError, KeyboardInterrupt):
        print("\nExiting...")
        break

    except Exception as e:
        print("\n=== Exception ===")
        print(traceback.format_exc())

        print("\n=== Incomplete Code String ===")
        print(pc.code_string)
