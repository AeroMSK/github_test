// 2026-09-24 - enum + match practice
use std::fmt;

#[derive(Debug, Clone, Copy)]
enum Shape {
    Circle(f64),
    Rect(f64, f64),
    Triangle(f64, f64),
}

impl Shape {
    fn area(&self) -> f64 {
        match self {
            Shape::Circle(r) => std::f64::consts::PI * r * r,
            Shape::Rect(w, h) => w * h,
            Shape::Triangle(b, h) => 0.5 * b * h,
        }
    }
}

impl fmt::Display for Shape {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "{:?} area = {:.2}", self, self.area())
    }
}

fn main() {
    let shapes = vec![
        Shape::Circle(3 as f64),
        Shape::Rect(3 as f64, 11 as f64),
        Shape::Triangle(8 as f64, 8 as f64),
    ];
    for s in &shapes {
        println!("{}", s);
    }
}
