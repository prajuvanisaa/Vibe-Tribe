import torch
import torch.nn as nn

class MusicGenerationModel(nn.Module):
    def __init__(self):
        super(MusicGenerationModel, self).__init__()
        self.lstm = nn.LSTM(input_size=3, hidden_size=128, num_layers=2, batch_first=True)
        self.fc = nn.Linear(128, 44100)  # Assuming output is a 1-second audio at 44.1kHz

    def forward(self, x):
        # Ensure the input is a tensor
        if not isinstance(x, torch.Tensor):
            raise ValueError("Input must be a torch.Tensor")

        # Check the input shape
        if x.dim() != 3:
            raise ValueError("Input tensor must have 3 dimensions: (batch_size, sequence_length, input_size)")

        # Pass through LSTM
        _, (hn, _) = self.lstm(x)

        # Only take the last hidden state
        output = self.fc(hn[-1])

        return output

# Example usage (for testing purposes)
if __name__ == "__main__":
    model = MusicGenerationModel()
    # Create a dummy input tensor with shape (batch_size, sequence_length, input_size)
    dummy_input = torch.rand(1, 10, 3)  # Batch size of 1, sequence length of 10, input size of 3
    output = model(dummy_input)
    print("Output shape:", output.shape)  # Should be (1, 44100)
