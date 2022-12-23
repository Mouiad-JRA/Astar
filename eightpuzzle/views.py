from django.shortcuts import render

from eightpuzzle.forms import AstarForm


def index(request):
    form = AstarForm()
    if request.method == "POST":
        form = AstarForm(request.POST)
        if form.is_valid():
            input_state = request.POST['input_state']
            end_state = request.POST['end_state']
            from eightpuzzle.algorthim import Puzzle
            puz = Puzzle(3)
            try:
                start = puz.accept(state=input_state)
                end = puz.accept(state=end_state)
            except Exception as e:
                print("The error is: " + e)

            result = puz.process(start, end)
            print(result)
            return render(request, 'result.html', {"result": result})

    return render(request, "eight-puzzle.html", {"form": form})
