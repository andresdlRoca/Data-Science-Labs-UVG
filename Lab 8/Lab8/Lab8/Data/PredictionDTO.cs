namespace Lab8.Data
{
    public class PredictionDTO
    {
        public string city { get; set; }
        public int rooms { get; set; } = 0;
        public int bathroom { get; set; } = 0;
        public int parking { get; set; } = 0;
        public int fireInsurance { get; set; } = 0;
        public string isFurnished { get; set; }
    }
}
