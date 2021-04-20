from rest_framework import serializers


class BaseOptionsSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    backgroundColor = serializers.CharField(default="rgba(171, 184, 195, 1)")
    dropShadow = serializers.BooleanField(default=True)
    dropShadowBlurRadius = serializers.CharField(default="68px")
    dropShadowOffsetY = serializers.CharField(default="20px")
    exportSize = serializers.CharField(default="2x")  #
    fontFamily = serializers.CharField(default="Hack")  #
    firstLineNumber = serializers.IntegerField(default=1)  #
    fontSize = serializers.CharField(default="14px")  #
    language = serializers.CharField(default="auto")  #
    lineHeight = serializers.CharField(default="133%")  #
    lineNumbers = serializers.BooleanField(default=False)  #
    paddingHorizontal = serializers.CharField(default="56px")  #
    paddingVertical = serializers.CharField(default="56px")  #
    squaredImage = serializers.BooleanField(default=False)  #
    theme = serializers.CharField(default="seti")  #
    watermark = serializers.BooleanField(default=False)  #
    widthAdjustment = serializers.BooleanField(default=True)  #
    windowControls = serializers.BooleanField(default=True)  #
    windowTheme = serializers.CharField(default="none")  #


class OptionsSerializer(BaseOptionsSerializer):
    def to_representation(self, instance):
        dict_values = super().to_representation(instance)
        for key, value in dict_values.items():
            if isinstance(value, bool):
                dict_values[key] = str(value).lower()

        params_dict = {
            "backgroundColor": "bg",
            "code": "code",
            "dropShadow": "ds",
            "dropShadowBlurRadius": "dsblur",
            "dropShadowOffsetY": "dsyoff",
            "exportSize": "es",
            "fontFamily": "fm",
            "firstLineNumber": "fl",
            "fontSize": "fs",
            "language": "l",
            "lineHeight": "lh",
            "lineNumbers": "ln",
            "paddingHorizontal": "ph",
            "paddingVertical": "pv",
            "squaredImage": "si",
            "theme": "t",
            "watermark": "wm",
            "widthAdjustment": "wa",
            "windowControls": "wc",
            "windowTheme": "wt",
        }

        carbon_dict = {}

        for key, value in params_dict.items():
            carbon_dict[value] = dict_values[key]

        return carbon_dict
