using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;
using OpenCV.Net;

[Combinator]
[Description("")]
[WorkflowElementCategory(ElementCategory.Transform)]
public class PenDigitizer
{
    public IObservable<Tuple<Point, IplImage>> Process(IObservable<Tuple<Point, IplImage>> source)
    {
        return source.Select(value => {
            var point = value.Item1;
            var image = value.Item2;
            CV.Circle(image, point, 5, Scalar.Rgb(255, 0, 0), -1);
            
            
            // Return the transformed point and image
            return Tuple.Create(point, image);
        });
    }
}