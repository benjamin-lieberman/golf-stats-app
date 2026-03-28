from django.shortcuts import render, redirect, get_object_or_404
from .models import Round, HoleStat
from .forms import RoundForm, HoleStatForm, PuttFormSet


def round_list(request):
    rounds = Round.objects.all().order_by("-date")
    return render(request, "rounds/round_list.html", {"rounds": rounds})


def round_create(request):
    form = RoundForm(request.POST or None)

    if form.is_valid():
        round_obj = form.save()

        # 🔥 create 18 holes automatically
        for i in range(1, 19):
            HoleStat.objects.create(
                round=round_obj,
                hole_number=i,
                par=4,  # default
            )

        return redirect("hole_entry", round_id=round_obj.id, hole_number=1)

    return render(request, "rounds/round_form.html", {"form": form})


def round_detail(request, round_id):
    round_obj = get_object_or_404(Round, id=round_id)
    holes = round_obj.holes.all().order_by("hole_number")

    return render(
        request,
        "rounds/round_detail.html",
        {"round": round_obj, "holes": holes},
    )


def hole_entry(request, round_id, hole_number):
    round_obj = get_object_or_404(Round, id=round_id)
    hole = get_object_or_404(
        HoleStat,
        round=round_obj,
        hole_number=hole_number
    )

    form = HoleStatForm(request.POST or None, instance=hole)
    formset = PuttFormSet(request.POST or None, instance=hole)

    if form.is_valid() and formset.is_valid():
        form.save()
        formset.save()

        # navigate to next hole
        if hole_number < 18:
            return redirect("hole_entry", round_id=round_id, hole_number=hole_number + 1)
        else:
            return redirect("round_detail", round_id=round_id)

    if not hole.putts.exists():
        initial_putts = [
            {"putt_number": 1},
            {"putt_number": 2},
            {"putt_number": 3},
        ]
    else:
        initial_putts = None

    formset = PuttFormSet(
        request.POST or None,
        instance=hole,
        initial=initial_putts
    )

    return render(
        request,
        "rounds/hole_entry.html",
        {
            "round": round_obj,
            "hole": hole,
            "form": form,
            "formset": formset,
        },
    )