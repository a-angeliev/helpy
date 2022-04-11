from django import forms


class BootstrapFormMixin:
    fields = {}

    def _init_bootstrap_form_controls(self):
        for _, field in self.fields.items():
            if not hasattr(field.widget, "attrs"):
                setattr(field.widget, "attrs", {})
            if "class" not in field.widget.attrs:
                field.widget.attrs["class"] = ""
            field.widget.attrs["class"] += " form-control"


class DisabledFieldsFormMixin:
    disabled_fields = "__all__"
    fields = {}

    def _init_disabled_fields(self):
        for name, field in self.fields.items():
            if self.disabled_fields != "__all__" and name not in self.disabled_fields:
                continue

            if not hasattr(field.widget, "attrs"):
                setattr(field.widget, "attrs", {})
            if isinstance(field, forms.ChoiceField):
                field.widget.attrs["disabled"] = "readonly"
            else:
                field.widget.attrs["readonly"] = "readonly"


class CityOption:
    SOFIA = "Sofia"
    PLOVDIV = "Plovdiv"
    VARNA = "Varna"
    BURGAR = "Burgas"
    RUSE = "Ruse"
    PLEVEN = "Pleven"
    SLIVEN = "Sliven"
    DOBRICH = "Dobrich"
    SHUMEN = "SHumen"
    PERNIK = "PERNIK"
    YAMBOL = "Yambol"

    CITYS = [
        [x, x]
        for x in (
            SOFIA,
            PLOVDIV,
            VARNA,
            BURGAR,
            RUSE,
            PLEVEN,
            SLIVEN,
            DOBRICH,
            SHUMEN,
            PERNIK,
            YAMBOL,
        )
    ]

    def max_city_length(self):

        return max(len(x) for x, _ in self.CITYS)


class PaymentOptions:
    SINGLE_PAYMENT = "Single payment"
    HOURLY = "Hourly"

    PAYMENT = [[x, x] for x in (SINGLE_PAYMENT, HOURLY)]

    def max_payment_length(self):
        return max(len(x) for x, _ in self.PAYMENT)


class PictureOptions:
    TOY = "/static/images/toy.png"
    PICTURES = [[x, x] for x in (TOY,)]

