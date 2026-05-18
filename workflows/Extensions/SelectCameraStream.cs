using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;

[Combinator]
[Description("")]
[WorkflowElementCategory(ElementCategory.Source)]
public class SelectCameraStream
{
    private event Action<string> CameraStreamChanged;
    private CameraStream cameraStream = CameraStream.CameraCenter;
    public CameraStream CameraStream 
    {
        get
        {
            return cameraStream;
        } 
        set
        {
            cameraStream = value;
            OnCameraStreamChanged(value);
        } 
    }
    private void OnCameraStreamChanged(CameraStream stream)
    {
        if (CameraStreamChanged != null)
        {
            CameraStreamChanged.Invoke(stream.ToString());
        }
    }
    public IObservable<string> Process()
    {
        return Observable.Defer(() => Observable.Return(cameraStream.ToString())).Concat(Observable.FromEvent<string>(handler => CameraStreamChanged += handler, handler => CameraStreamChanged -= handler));
    }
}

public enum CameraStream
{
    CameraBottomLeft,
    CameraBottomRight,
    CameraCenter,
    CameraLeft,
    CameraRight,
    CameraTop,
    CameraTopLeft,
    CameraTopRight
}
