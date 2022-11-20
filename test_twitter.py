from twttr import shorten

def main():
    test_twttr()

def test_twttr():
    assert shorten("twitter") == "twttr"
    assert shorten("language") == "lngg"
    assert shorten("weee") == "w"
    assert shorten("Aoo FUck") == " Fck"

if __name__ == "__main__":
    main() 