package models

import "time"

type Card struct {
	Title     string    `json:"title"`
	UserID    int       `json:"user_id"`
	BoardID   int       `json:"board_id"`
	CreatedAt time.Time `json:"created_at"`
}
