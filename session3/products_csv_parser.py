import csv


def main(args):
    out_filename = input('Enter the filename of the CSV output file: ')

    with open(args.file, 'r') as infile, open(out_filename, 'w') as outfile:
        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            if row['Categories'] != '':
                writer.writerow(row)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        'file',
        help='CSV input file',
    )
    args = parser.parse_args()

    main(args)
