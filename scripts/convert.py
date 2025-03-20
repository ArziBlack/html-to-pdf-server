# scripts/convert.py
import sys
from weasyprint import HTML

def main():
    if len(sys.argv) != 3:
        print("Usage: python convert.py <input_html> <output_pdf>")
        sys.exit(1)

    input_html = sys.argv[1]
    output_pdf = sys.argv[2]

    try:
        HTML(input_html).write_pdf(output_pdf)
        print(f"PDF successfully created at {output_pdf}")
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()