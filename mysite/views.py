# This file is created by dx
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


# text_analyzer
def analyze(request):
    # get the text value
    dj_text = request.POST.get("main_text", "default")
    dj_text2 = request.POST.get("main_text2","default")
    word_count = request.POST.get("word_count", "off")
    punc = request.POST.get("punc", "off")
    upper = request.POST.get("upper", "off")
    newlineremover = request.POST.get("newlineremover", "off")
    charcount = request.POST.get("charcount", "off")
    spaceremover = request.POST.get("spaceremover", "off")

    # analyze part
    if dj_text2 != "":
        analyzed = len(dj_text2)
        print(dj_text2)
        print(analyzed)
        params = {
            "purpose":"Character Counter",
            "results": f"Total Letters Present: {analyzed} \nOrignal Word: {dj_text2}",
        }
        return render(request,"analyze.html", params)
    if punc == "on":
        punctuation = '''o/?@#$%^&*_~'''
        punc_results = ""
        for char in dj_text:
            if char not in punctuation:
                punc_results = punc_results + char
        # print(punc_results)
        params = {
            'purpose': "Punctuation Remover Tool (Except . and ,)",
            'results': punc_results,
            "original": dj_text,
        }
        dj_text = punc_results
        # return render(request, "analyze.html", params)

    if newlineremover == "on":
        analyzed = ""
        for char in dj_text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        print(analyzed)

        dj_text = analyzed

        params = {
            'purpose': " New Line Remover Tool",
            'results': analyzed,
        }

    if spaceremover == "on":
        analyzed = ""
        for index, char in enumerate(dj_text):
            if not (dj_text[index] == " " and dj_text[index + 1] == " "):
                analyzed = analyzed + char

        dj_text = analyzed

        params = {
            'purpose': " Space Remover Tool",
            'results': analyzed,
        }

    if upper == "on":
        upper_text = ""
        upper_text = dj_text.upper()
        print(upper_text)

        params = {
            'purpose': " UpperCase Maker Tool",
            'results': upper_text,
        }

        dj_text = upper_text
    # if word_count == "on":
    #     count = 0
    #     list = dj_text.split()
    #     count = len(list)
    #
    #     params = {
    #         'purpose': "Word Count Tool",
    #         'results': str(count) + " ",
    #         'letter_count': "",
    #         'word_count': "Word Count: ",
    #         'result_letter': "",
    #         'result_word': str(count),
    #     }
    #
    #     # return render(request, "analyze.html", params)
    #     # return render(request,"analyze.html", params)
    #
    # if charcount == "on":
    #     analyzed = ""
    #     for char in dj_text:
    #         if char != " ":
    #             analyzed = analyzed + char
    #             print(analyzed)
    #     analyzed = len(analyzed)
    #     print(analyzed)
    #
    #     params = {
    #         'purpose': " Character Counter Tool",
    #         'results': analyzed,
    #         'letter_count': "Letter Count: ",
    #         'word_count': "",
    #         'result_letter':analyzed,
    #         'result_word':"",
    #     }

    if punc != "on" and upper != "on" and  newlineremover != "on" and spaceremover != "on":
        return HttpResponse("ERROR (NOTHING SELECTED)")

    return render(request, "analyze.html", params)
