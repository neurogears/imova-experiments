using System;
using Bonsai.Gui;

class TextBoxAutoFocusVisualizer : TextBoxVisualizer
{
    public override void Show(object value)
    {
        base.Show(value);
        Control.Focus();
    }
}