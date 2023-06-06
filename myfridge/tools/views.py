from django.shortcuts import render
from .forms import BMIForm


def bmiView(request):
    if request.method == "POST":
        form = BMIForm(request.POST)
        if form.is_valid():
            bmi = form.calculate_bmi()
            bmi_result = form.return_bmi_result()
            return render(
                request, "bmi_result.html", {"bmi": bmi, "bmi_result": bmi_result}
            )
    else:
        form = BMIForm()

    return render(request, "bmi_form.html", {"form": form})
