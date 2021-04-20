from rest_framework import serializers


class BaseOptionsSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)  # Code
    bg = serializers.CharField(default="rgba(171, 184, 195, 1)")  # Background
    ds = serializers.BooleanField(default=True)  # dropShadow
    dsblur = serializers.CharField(default="68px")  # dropShadowBlurRadius
    dsyoff = serializers.CharField(default="20px")  # dropShadowOffsetY
    es = serializers.CharField(default="2x")  # exportSize
    fm = serializers.CharField(default="Hack")  # fontFamily
    fl = serializers.IntegerField(default=1)  # firstLineNumber
    fs = serializers.CharField(default="14px")  # fontSize
    l = serializers.CharField(default="auto")  # language
    lh = serializers.CharField(default="133%")  # lineHeight
    ln = serializers.BooleanField(default=False)  # lineNumbers
    ph = serializers.CharField(default="56px")  # paddingHorizontal
    pv = serializers.CharField(default="56px")  # paddingVertical
    si = serializers.BooleanField(default=False)  # squaredImage
    t = serializers.CharField(default="seti")  # theme
    wm = serializers.BooleanField(default=False)  # watermark
    wa = serializers.BooleanField(default=True)  # widthAdjustment
    wc = serializers.BooleanField(default=True)  # windowControls
    wt = serializers.CharField(default="none")  # windowTheme


class OptionsSerializer(BaseOptionsSerializer):
    def to_representation(self, instance):
        dict_values = super().to_representation(instance)
        for key, value in dict_values.items():
            if isinstance(value, bool):
                dict_values[key] = str(value).lower()
        return dict_values
