def test_title():
    with open("index.html", "r", encoding="utf-8") as f:
        content = f.read()
    assert "Hola Mundo" in content
