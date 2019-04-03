from vklabs.tika import parser

proxy = {
    'http': '',
    'https': ''
}


def tika_run():
    pdf_url = "https://www.adobe.com/support/products/enterprise/knowledgecenter/media/c4611_sample_explain.pdf"
    pdf_dict = parser.from_file(
        filename=pdf_url,
        # proxy=proxy,
    )
    if pdf_dict.get("status"):
        print(pdf_dict)
    else:
        print("{}\n{}\n{}".format(pdf_dict["metadata"]["Author"], pdf_dict["metadata"]["title"], pdf_dict["content"]))


if __name__ == '__main__':
    tika_run()
