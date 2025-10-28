using Bonsai;
using System;
using System.ComponentModel;
using System.Collections.Generic;
using System.Linq;
using System.Reactive.Linq;
using Microsoft.CodeAnalysis.CSharp;

[Combinator]
[Description("transform a string into a C# literal representation.")]
[WorkflowElementCategory(ElementCategory.Transform)]
public class ToLiteral
{
    public IObservable<string> Process(IObservable<string> source)
    {
        return source.Select(value => SymbolDisplay.FormatLiteral(value, false));
    }
}
